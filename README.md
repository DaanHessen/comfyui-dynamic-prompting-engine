<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/DaanHessen/comfyui-dynamic-prompting-engine">
    <!-- Replace with actual logo if you have one! -->
    <img src="https://raw.githubusercontent.com/comfyanonymous/ComfyUI/master/comfyui_screenshot.png" alt="Logo" width="400">
  </a>

<h3 align="center">ComfyUI Dynamic Prompting Engine</h3>

  <p align="center">
    A robust ComfyUI custom node suite for advanced string parsing, dynamic text inputs, nested randomness, and dynamic resolution pooling.
    <br />
    <a href="https://github.com/DaanHessen/comfyui-dynamic-prompting-engine"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/DaanHessen/comfyui-dynamic-prompting-engine/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/DaanHessen/comfyui-dynamic-prompting-engine/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Generating complex, varied datasets and exploring latent spaces requires robust text composition. The **Dynamic Prompting Engine** allows you to feed multiline string blueprints into ComfyUI, utilizing completely dynamic widget inputs and advanced randomization features directly from the UI. No messy arrays, no complex looping structures—just intuitive prompts.

Key Features:
* **Dynamic Node Sockets:** Wrap `{any_word}` in curly brackets in the main template string and the node instantly spawns a matching text input port for you to connect external strings.
* **Nested Randomness (Pipes):** Use `{A|B|C}` notation to randomize broader categories in the master template before randomly selecting lines from those chosen categories.
* **Weighted Probabilities:** Scale your pipe branches easily using the double colon syntax `{10::A|1::B}` to make choice A ten times more likely to roll! 
* **Multi-Selection Generation:** Need exactly three randomized inputs from the same variable block? Prefix the category with money signs `{3$$ red | green | blue | black}` to securely spawn "red, black, green" directly onto one string without duplicates. 
* **Direct Wildcards (`__text__`):** Seamlessly scan your local `wildcards` folder! Adding `__clothing__` natively bypasses node-socket generation and instead parses lines directly out of `clothing.txt` line-by-line off your hard drive. 
* **Resolution Pooling:** Automatically generate dataset-ready outputs and extract sizes via inline `--res` tagging directly into your generation loop without requiring extra Nodes. 
* **Seamless On-Node UI Preview:** Immediately see what you built! The node constructs a semi-transparent `Output` widget on its own surface post-execution to display the generated string and resolution choices locally. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python]][Python-url]
* [![JavaScript][JavaScript]][JavaScript-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these simple installation steps.

### Prerequisites

Ensure you have a working installation of [ComfyUI](https://github.com/comfyanonymous/ComfyUI) running on your local machine.

### Installation

1. Navigate to your ComfyUI `custom_nodes` folder
   ```sh
   cd D:/comfy/ComfyUI/custom_nodes/
   ```
2. Clone the repo
   ```sh
   git clone https://github.com/DaanHessen/comfyui-dynamic-prompting-engine.git
   ```
3. Restart your ComfyUI terminal/server to automatically compile and serve the backend/frontend components.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

After installation, search your ComfyUI double-click menu for the `utils` category. You will find standard elements such as:
- **Dynamic Template Prompt Builder**: Connect a seed. Type dynamic tags directly like `{subject}` into your template block. Watch new ports explicitly spawn on the node interface to pipe text arrays straight into it!
- **String with Resolution Pool**: Merge multiline string descriptions with a stack of resolutions to automatically format text chunks identically to `1024x1024` randomness parameters inline.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Basic string building using curly brackets
- [x] Nested Randomness functionality (Piped inputs)
- [x] Embedded Resolution Pool extraction
- [x] Direct wildcards integration (`__wildcard__`)
- [x] Multi-selection pooling (`$$`)
- [x] Node-based text execution preview
- [x] Weighted Randomness Probability (`::`)

See the [open issues](https://github.com/DaanHessen/comfyui-dynamic-prompting-engine/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/DaanHessen/comfyui-dynamic-prompting-engine/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DaanHessen/comfyui-dynamic-prompting-engine" alt="contrib.rocks image" />
</a>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Daan Hessen - [GitHub: DaanHessen](https://github.com/DaanHessen)

Project Link: [https://github.com/DaanHessen/comfyui-dynamic-prompting-engine](https://github.com/DaanHessen/comfyui-dynamic-prompting-engine)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/DaanHessen/comfyui-dynamic-prompting-engine.svg?style=for-the-badge
[contributors-url]: https://github.com/DaanHessen/comfyui-dynamic-prompting-engine/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DaanHessen/comfyui-dynamic-prompting-engine.svg?style=for-the-badge
[forks-url]: https://github.com/DaanHessen/comfyui-dynamic-prompting-engine/network/members
[stars-shield]: https://img.shields.io/github/stars/DaanHessen/comfyui-dynamic-prompting-engine.svg?style=for-the-badge
[stars-url]: https://github.com/DaanHessen/comfyui-dynamic-prompting-engine/stargazers
[issues-shield]: https://img.shields.io/github/issues/DaanHessen/comfyui-dynamic-prompting-engine.svg?style=for-the-badge
[issues-url]: https://github.com/DaanHessen/comfyui-dynamic-prompting-engine/issues
[license-shield]: https://img.shields.io/github/license/DaanHessen/comfyui-dynamic-prompting-engine.svg?style=for-the-badge
[license-url]: https://github.com/DaanHessen/comfyui-dynamic-prompting-engine/blob/master/LICENSE.txt
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[JavaScript]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
