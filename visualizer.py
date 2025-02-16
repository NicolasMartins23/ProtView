import py3Dmol

def visualize_pdb(pdb_string, style="cartoon"):
    """Generates an interactive HTML visualization for a PDB file."""
    
    view = py3Dmol.view(width=800, height=600)
    view.addModel(pdb_string, "pdb")
    
    # Apply user-selected style
    if style.lower() == "cartoon":
        view.setStyle({"cartoon": {"color": "spectrum"}})
    elif style.lower() == "stick":
        view.setStyle({"stick": {}})
    elif style.lower() == "sphere":
        view.setStyle({"sphere": {}})

    view.zoomTo(1.5)
    
    return view._make_html()
