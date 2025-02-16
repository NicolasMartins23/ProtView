import py3Dmol

class ProteinVisualizer:
    def __init__(self, file_data: str, file_extension: str):
        """
        Initializes the ProteinVisualizer instance.
        
        :param file_data: The file contents (PDB or CIF format) as a string.
        :param file_extension: The extension of the file ("pdb" or "cif").
        """
        self.file_data = file_data
        self.file_extension = file_extension.lower()
    
    def _add_model(self, view: py3Dmol.view) -> None:
        """
        Adds the model to the 3Dmol viewer based on the file extension.
        
        :param view: The 3Dmol view object where the model will be added.
        """
        if self.file_extension == "pdb":
            view.addModel(self.file_data, "pdb")
        elif self.file_extension == "cif":
            view.addModel(self.file_data, "cif")
        else:
            raise ValueError("Unsupported file format. Only PDB and CIF are supported.")
    
    def generate_visualization(self, style: str = "cartoon") -> str:
        """
        Generates an interactive 3D molecular visualization.
        
        :param style: The visualization style ("cartoon", "stick", "sphere").
        :return: The HTML content for embedding in a web application.
        """
        view = py3Dmol.view(width=800, height=600)
        
        # Add the model based on the file type
        self._add_model(view)
        
        # Apply the style chosen by the user
        if style.lower() == "cartoon":
            view.setStyle({"cartoon": {"color": "spectrum"}})
        elif style.lower() == "stick":
            view.setStyle({"stick": {}})
        elif style.lower() == "sphere":
            view.setStyle({"sphere": {}})
        else:
            raise ValueError(f"Unsupported style: {style}. Choose 'cartoon', 'stick', or 'sphere'.")
        
        # Zoom in on the structure and render it
        view.zoomTo(1.5)
        
        # Return the HTML content for rendering
        return view._make_html()
