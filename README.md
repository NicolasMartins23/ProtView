# 3D Protein Structure Visualizer
🔬 3D Protein Structure Visualizer is a web app built with Streamlit that allows you to upload a PDB file and visualize its molecular structure in 3D.<br/>
The app supports different visualization styles (e.g., Cartoon, Stick, Sphere) and offers interactive controls to explore the protein structure.<br/>
The online version can be acessed here: https://bioapps-protview.streamlit.app/ <br>

# Features
- Upload and visualize PDB files in 3D.
- Choose between three different molecular visualization styles: Cartoon, Stick, Sphere
- Interactive controls for rotating, zooming, and moving the structure.

# Requirements
- Python 3.7+
- Streamlit
- py3Dmol
- Can be installed via requirements.txt

# Installation
### Clone the repository:

git clone https://github.com/NicolasMartins/ProtView.git<br/>
cd ProtView

### Install the required dependencies:
pip install -r requirements.txt

### Run the app:
streamlit run app.py

# How to Use
### Uploading a file
Upload a PDB File: Click on the "Upload a PDB file" button to select a PDB file from your computer.<br/>
An example PDB file is present on the repository<br/>
Choose a Visualization Style: Select the style of visualization from the dropdown menu. Default is cartoon.<br/>
### View Controls:<br/>
Rotate: Left-click and drag to rotate the structure.<br/>
Zoom: Hold Shift + Left-click or scroll to zoom in/out.<br/>
Move: Hold Control + Left-click and drag to move the structure.<br/>
On-screen instructions are provived.<br/>

### Project Structure
├── app.py                # Main Streamlit app<br/>
├── example.pdb           # Example pdb file for ease of use<br/>
├── visualizer.py         # Python script for 3Dmol visualization<br/>
├── requirements.txt      # List of dependencies<br/>
└── README.md             # Project documentation<br/>

