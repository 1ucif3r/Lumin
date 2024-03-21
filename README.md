<p align=center>
  <img title="Built With Love" src="https://forthebadge.com/images/badges/built-with-love.svg"></p>

<br>

<p align=center>
  <a href="https://github.com/1ucif3r"><img title="Made in INDIA" src="https://img.shields.io/badge/MADE%20IN-INDIA-SCRIPT?colorA=%23ff8100&colorB=%23017e40&colorC=%23ff0000&style=for-the-badge"></a>
  </p>

<p align="center">
  <img src="https://github.com/1ucif3r/Lumin/blob/main/luminlogo.png" alt=" Logo" />
</p>

<br>

### <p align="center">LUMIN<p align="center">

<p align=center>
  <a href="https://github.com/1ucif3r"><img title="Open Source" src="https://img.shields.io/badge/Open%20Source-%E2%99%A5-red" ></a>
  <a href="https://github.com/1ucif3r"><img title="GitHub version" src="https://d25lcipzij17d.cloudfront.net/badge.svg?id=gh&type=6&v=1.0&x2=0" ></a>
  <a href="https://github.com/1ucif3r"><img title="Stars" src="https://img.shields.io/github/stars/1ucif3r/Lumin?style=social" ></a>
  <a href="https://github.com/1ucif3r/network/members"><img title="Forks" src="https://img.shields.io/github/forks/1ucif3r/Lumin?color=red&style=flat-square"></a>
  <a href="https://github.com/1ucif3r"><img title="Watching" src="https://img.shields.io/github/watchers/1ucif3r/Lumin?label=Watchers&color=blue&style=flat-square"></a>

###### <p align="center"> *This is official repository maintained by Us.*

###### <p align="center"> Made with ❤️ By [**1ucif3r**](https://github.com/1ucif3r)

###### <p align="center">LUMIN is a advance collections of steganography tools designed to securely conceal sensitive information within images , videos & Other Files . It stands out in the realm of digital steganography by combining advanced encryption, compression, and a seeded Least Significant Bit (LSB) technique to provide a robust solution for embedding data undetectably.<p align="center">

## Key Features

- **Advanced Encryption**: Lumin's tools uses AES-256 encryption for the data, with a session key that is further encrypted using RSA public key cryptography. This two-tier encryption ensures that only the holder of the corresponding RSA private key can decrypt the hidden information, providing a high level of security.

- **Compression**: Before encryption, the data is compressed using zlib to reduce its size. This not only makes the process more efficient but also helps in minimizing patterns that could be detected by steganalysis tools.

- **Seeded LSB Steganography**: The tool employs a seeded random number generator to determine the pixel positions used for embedding the data. This approach scatters the hidden bits throughout the image, making it more resistant to detection by steganalysis tools like zsteg.

- **File Name Storage**: Lumin's tools stores the original filename of the hidden data within the image. This allows for the file to be extracted with its original name, providing additional convenience and maintaining file identity.

- **Cross-Platform Compatibility**: Written in Python, Lumin is cross-platform and can be used on any system with Python installed.


## Installation [Linux](https://wikipedia.org/wiki/Linux) [![alt tag](http://icons.iconarchive.com/icons/dakirby309/simply-styled/32/OS-Linux-icon.png)](https://fr.wikipedia.org/wiki/Linux)

To use Lumin, clone the repository or download the source code from GitHub. Ensure you have Python 3 installed on your system, along with the required packages:

```
git clone https://github.com/1ucif3r/Lumin.git
cd Lumin
pip3 install -r requirements.txt

python3 main.py
```

## Security Note

While using Lumin's tool uses strong encryption algorithms, security also depends on the RSA key strength, private key secrecy, and passphrase strength. Keep your private key secure and use a strong passphrase.
