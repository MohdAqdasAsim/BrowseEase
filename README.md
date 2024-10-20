<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">BrowseEase</h3>

  <p align="center">
    Streamline your browsing experience from the console with BrowseEase.
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](/)

There are many tools available for quick browsing, but BrowseEase was created as a streamlined solution to enhance your browsing experience directly from the console. Here’s why BrowseEase stands out:

- **Efficiency at its core**: This project is designed for users who want a faster way to open browsers and navigate to their favorite sites without manual typing.
- **Clear and accessible code**: The codebase is available for anyone to explore, showcasing how to implement simple command-line interactions in Python.
- **User-friendly experience**: Launch websites with just a few commands, making your browsing as easy and quick as possible.
  
This project is continually evolving. If you’d like to contribute or suggest improvements, feel free to check out the repository and get involved in simplifying browsing workflows!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

1. Python
  ```sh
  # For Windows
  winget install Python.Python

  # For macOS
  brew install python

  # For Linux (Debian-based)
  sudo apt update
  sudo apt install python3
  ```

2. After installation, you can verify that Python is installed by running:
   ```sh
   python --version  # or python3 --version on some systems
   ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/MohdAqdasAsim/BrowseEase.git
   ```
   
2. **Create an Alias for Quick Access**

   To set up an alias for the BrowseEase script, follow these instructions for your operating system:

   - **Windows (Command Prompt)**
     1. Open Command Prompt.
     2. Use the following command to create an alias (replace `path_to_your_script` with the actual path to your script):
        ```cmd
        doskey browseease=python path_to_your_script/browseease.py $*
        ```

   - **Linux and macOS**
     1. Open a terminal.
     2. Edit your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`):
        ```sh
        nano ~/.bashrc  # or nano ~/.zshrc for Zsh users
        ```
     3. Add the following line at the end of the file (replace `path_to_your_script` with the actual path):
        ```sh
        alias browseease='python path_to_your_script/browseease.py'
        ```
     4. Save the file and exit the editor. 
     5. Apply the changes by running:
        ```sh
        source ~/.bashrc  # or source ~/.zshrc for Zsh users
        ```

3. **Verify the Alias**

   After setting up the alias, you can verify it by running:
   ```sh
   browseease
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Screenshots

Here are some more screenshots of the website:

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions make the open-source community such an incredible place to learn, inspire, and innovate. Any contributions you make are **greatly appreciated** and help enhance this project.

If you have a suggestion to improve the project, feel free to fork the repo and submit a pull request. You can also open an issue with the "enhancement" tag. Don't forget to give the project a star if you find it helpful—thanks for your support!

Steps to Contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Mohd Aqdas Asim - [@mohdaqdasasim](https://www.linkedin.com/in/mohd-aqdas-asim/) - mohdaqdasasim@gmail.com

Project Link: [https://github.com/MohdAqdasAsim/BrowseEase](https://github.com/MohdAqdasAsim/BrowseEase)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/MohdAqdasAsim/Beyond-Realms.svg?style=for-the-badge
[contributors-url]: https://github.com/MohdAqdasAsim/Beyond-Realms/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/MohdAqdasAsim/Beyond-Realms.svg?style=for-the-badge
[forks-url]: https://github.com/MohdAqdasAsim/Beyond-Realms/network/members
[license-shield]: https://img.shields.io/github/license/MohdAqdasAsim/Beyond-Realms.svg?style=for-the-badge
[license-url]: https://github.com/MohdAqdasAsim/Beyond-Realms/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mohd-aqdas-asim/
[product-screenshot]: /mockups/mockup-1.png
