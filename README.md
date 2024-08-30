# CursedWords

Welcome to the **CursedWords** repository, a community-driven project dedicated to identifying and eliminating overused, clichéd, and predictable language from AI-generated content.

## 🚨 What is "CursedWords"?

In the rapidly evolving world of AI, certain words and phrases have become overused to the point of predictability, making AI-generated content feel mechanical and uninspired. This repository is a collective effort to **get rid of this nightmare** by curating a list of such "cursed words" that anyone can contribute to or use to fine-tune their language models.

## 🌟 How to Contribute

We welcome contributions from everyone! Here's how you can participate:

1. **Fork** this repository.
2. **Add** your overused words or phrases to the `CursedWords.txt` file.
3. **Submit** a Pull Request with your additions.

### 🤖 Multion Agent Validation

To maintain the quality and relevance of this repository, we've implemented a **Multion agent** to assess new contributions:

* When you submit a new word or phrase, our validation script will prompt the Multion agent with the current list of cursed words.
* The agent will evaluate the likelihood of the new submission being overused or irrelevant.
* If the submission is deemed not overused, it will be automatically rejected to keep our list clean and focused.

### 📝 Appeal Process

We understand that AI isn't perfect. If your submission is rejected by the Multion agent, but you believe it should be included:

* **Open a PR** labeled as an appeal and provide a justification for why the word or phrase belongs on the list.
* The community and maintainers will discuss the appeal in the PR thread.
* If consensus is reached, the submission will be manually added to the `CursedWords.txt` file.

This approach ensures that only genuinely overused phrases make it into the repository, while still allowing for human oversight and discussion.

## 🔄 Keeping Formats in Sync

The `CursedWords.txt` file serves as the master list. Whenever a change is made:

* A script automatically updates the `CursedWords.json` and `index.html` files.
* This ensures that all formats are consistent and up-to-date.

These files are available on our GitHub Pages site at [xuede.github.io/CursedWords](https://xuede.github.io/CursedWords), where they can be accessed for fine-tuning language models.

## 🔍 Monitoring and Maintenance with Multion

We also use Multion's powerful API and agents as custodians to:

* **Monitor** the repository every 6 hours for defacement or inappropriate content.
* **Automatically remediate** and flag any PRs or commits that violate our guidelines.

## 🤖 For AI Developers

Fine-tuning your models? Use this repository as a resource to help your AI break free from the chains of overused language. By avoiding these "cursed words," your models can produce more original and engaging content.
