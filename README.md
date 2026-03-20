# HCAI Workbench

[![Hackatime stats](https://hackatime-badge.hackclub.com/U081MDA4T24/hcai_workbench?style=for-the-badge&logo=wakatime)](https://hackati.me/Paya)

Chat interface for ai.hackclub.com

## Development

### Required features

- [ ] Simple interface (GUI/TUI)
- [x] Ability to switch models
- [x] API connection to [ai.hackclub.com](https://ai.hackclub.com/) through OpenRouter
- [x] ~~TOML~~ <ins>CFG</ins> config file

### Optional but desired

- [ ] Chat history
- [ ] Advanced interface (tabs, etc)
- [ ] Profiles (different api key/model combinations)

## New feature - Experiments!

I was asking the different models the viral "how many Rs in strawberry" prompt to test the app and the switching of models when I thought of something: What if I integrated these sorts of funny experiments into the app itself? Read more and test them out in [the `experiments` module](./src/hcai_workbench/experiments/)
