// Drafts → GitHub: Create a blog post in /posts for larrieknights.com

// 1. GitHub credentials
let githubCredential = Credential.create(
    "GitHub more of less",
    "Enter your GitHub details for posting to your more-of-less repository."
);

githubCredential.addTextField("username", "Username");
githubCredential.addPasswordField("token", "Personal Access Token");
githubCredential.addTextField("repoName", "Repository Name");
githubCredential.addTextField("email", "Email Address");

if (!githubCredential.authorize()) {
    console.log("Authorization failed or was cancelled by the user.");
    context.fail();
}

const username = githubCredential.getValue("username");
const token = githubCredential.getValue("token");
const repoName = githubCredential.getValue("repoName");
const email = githubCredential.getValue("email");

// 2. Prepare metadata from the Draft
const lines = draft.content.split("\n");
const rawTitle = (lines[0] || "").replace(/^#\s*/, "").trim();
const title = rawTitle || "Untitled";

const today = new Date().toISOString().split("T")[0];

const baseSlug = title
    .toLowerCase()
    .replace(/[^\w\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");

// 3. Helper: check whether a file already exists on GitHub
function githubFileExists(path) {
    const url = `https://api.github.com/repos/${username}/${repoName}/contents/${path}`;

    let http = HTTP.create();
    let response = http.request({
        url: url,
        method: "GET",
        headers: {
            Authorization: `Bearer ${token}`,
            "User-Agent": "DraftsApp",
            "X-GitHub-Api-Version": "2022-11-28"
        }
    });

    return response.statusCode === 200;
}

// 4. Helper: find a unique slug / filename
function getUniqueSlug(baseSlug) {
    let slug = baseSlug;
    let counter = 2;

    while (githubFileExists(`posts/${slug}.md`)) {
        slug = `${baseSlug}-${counter}`;
        counter++;
    }

    return slug;
}

const slug = getUniqueSlug(baseSlug);
const fileName = `${slug}.md`;

// 5. Construct frontmatter
const frontMatter = `---
title: ${title}
date: ${today}
slug: ${slug}
---
`;

// Body is everything after the first line
const body = lines.slice(1).join("\n");
const fullContent = frontMatter + "\n" + body;

// Base64 encode for GitHub API
const encodedContent = Base64.encode(fullContent);

// 6. GitHub API: create file in /posts/
const path = `posts/${fileName}`;
const apiUrl = `https://api.github.com/repos/${username}/${repoName}/contents/${path}`;

const data = {
    message: `Create post: ${title}`,
    committer: {
        name: username,
        email: email
    },
    content: encodedContent
    // branch: "main"
};

// 7. HTTP request
let http = HTTP.create();
let response = http.request({
    url: apiUrl,
    method: "PUT",
    headers: {
        Authorization: `Bearer ${token}`,
        "User-Agent": "DraftsApp",
        "Content-Type": "application/json",
        "X-GitHub-Api-Version": "2022-11-28"
    },
    data: data
});

// 8. Process response
if (response.statusCode === 200 || response.statusCode === 201) {
    console.log("Successfully created/updated the file on GitHub at: " + path);
} else {
    console.log(
        "Failed to post to GitHub. Status code: " +
        response.statusCode +
        " Response: " +
        response.responseText
    );
}