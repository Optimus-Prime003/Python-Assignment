# Ubuntu Image Fetcher

Ubuntu Image Fetcher is a simple Python tool that allows you to download
and save images from the web.\
It ensures that only valid image files are fetched, prevents duplicates,
and saves them neatly in a folder.

------------------------------------------------------------------------

## ✨ Features

-   Fetch multiple images from URLs at once.
-   Automatically detects valid image files (based on content type).
-   Generates unique filenames for images without proper names.
-   Prevents duplicate downloads (by comparing content).
-   Saves all images inside a `Fetched_Images` folder.

------------------------------------------------------------------------

## 📂 Project Structure

    .
    ├── Fetched_Images/    # Folder where downloaded images are stored
    ├── fetcher.py         # Main Python script
    └── README.md          # Project documentation

------------------------------------------------------------------------

## 🚀 How to Use

### 1. Clone or Download the Project

``` bash
git clone <your-repo-link>
cd <project-folder>
```

### 2. Install Requirements

This project uses the `requests` library. Install it with:

``` bash
pip install requests
```

### 3. Run the Script

``` bash
python Ubuntu_Image_Fetcher.py
```

### 4. Input Image URLs

When prompted, enter one or more image URLs separated by commas:

    Enter image URLs separated by commas:
    https://example.com/image1.jpg, https://example.com/image2.png

The images will be downloaded into the `Fetched_Images` folder.

------------------------------------------------------------------------

## ⚡ Example Run

    Welcome to the Ubuntu Image Fetcher
    A tool for mindfully collecting images from the web

    Enter image URLs separated by commas:
    https://via.placeholder.com/150, https://via.placeholder.com/300

    ✓ Successfully fetched: 150
    ✓ Image saved to Fetched_Images/150

    ✓ Successfully fetched: 300
    ✓ Image saved to Fetched_Images/300

    Connection strengthened. Community enriched.

------------------------------------------------------------------------

## 🛠 Requirements

-   Python 3.7+
-   `requests` library

Install dependencies with:

``` bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can create one using:

``` bash
pip freeze > requirements.txt
```

------------------------------------------------------------------------

## 🤝 Contribution

Feel free to fork this project and enhance it with new features such
as: - Download progress bar - URL validation before fetching - Async
support for faster downloads

------------------------------------------------------------------------

## 📜 License

This project is open-source and available under the MIT License.
