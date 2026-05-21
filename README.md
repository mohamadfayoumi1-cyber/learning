# Mohamad Fayoumi CV Website

This is a static CV website for Mohamad Fayoumi. It is designed to be published as a public GitHub Pages site.

## How to publish

### Option 1: Push to GitHub and use the built-in workflow

1. Open your project folder in a Git client or GitHub Desktop.
2. Commit all changes.
3. Push to `main` branch.

The included workflow file `.github/workflows/pages.yml` will publish the site to the `gh-pages` branch automatically.

### Option 2: Use GitHub web upload

1. Go to `https://github.com/mohamadfayoumi1-cyber/learning`.
2. Upload `index.html`, `styles.css`, `script.js`, and `.github/workflows/pages.yml`.
3. Commit the changes.

### Option 3: Deploy on Vercel

1. Sign in to https://vercel.com with your GitHub account.
2. Click "New Project" and import the `mohamadfayoumi1-cyber/learning` repository.
3. Use the default settings; Vercel detects the static HTML site automatically.
4. If Vercel asks for a framework, choose "Other" or "Static Site".
5. Deploy the project.

After the first deploy, Vercel will give you a public URL like `https://<project-name>.vercel.app/`.

### After publishing

Once the repository is pushed, GitHub Actions will deploy the site. The expected URL is:

`https://mohamadfayoumi1-cyber.github.io/learning/`

If the repository is later renamed to `mohamadfayoumi1-cyber.github.io`, the site will be available at:

`https://mohamadfayoumi1-cyber.github.io/`

## If you want to use Git locally

If Git is installed, run:

```bash
cd c:\Users\user\Documents\GitHub\learning
git add .
git commit -m "Publish CV website"
git push origin main
```

## If Git is not installed

Use GitHub Desktop or the GitHub web interface to upload the files and commit them to the `main` branch.

## Notes

- Your site metadata already includes a title, description, keywords, Open Graph tags, and canonical URL.
- Search engines will only index the site after it is publicly available.
- It may take a few hours or days for `Mohamad Fayoumi` to show in search results.
