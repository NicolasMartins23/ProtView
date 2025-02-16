import streamlit as st
from visualizer import visualize_pdb

st.title("🔬 3D Protein Structure Visualizer")
st.write("Upload a **PDB file** to visualize its molecular structure.")

# Upload PDB file
uploaded_file = st.file_uploader("Upload a PDB file", type=["pdb"])

if uploaded_file is not None:
    pdb_data = uploaded_file.read().decode("utf-8")
    
    # Display PDB file preview
    st.subheader("📄 PDB File Preview:")
    st.code("\n".join(pdb_data.split("\n")[:20]))  # Show first 20 lines

    # 🧬 3D Molecular Visualization
    st.subheader("🧬 3D Molecular Visualization:")
    
    # Dropdown for visualization style
    style_options: list[str] = ["Cartoon", "Stick", "Sphere"]
    style = st.radio(
        label="Visualization",
        options=style_options,
        index=0,
        horizontal=True
    )

    # Generate HTML visualization
    html_content = visualize_pdb(pdb_data, style)
    st.components.v1.html(html_content, height=700, width=900, scrolling=True)

    # ⚙️ Controls Section
    st.subheader("⚙️ Controls:")
    st.write("Rotate: Left Click")
    st.write("Zoom: Shift + Left Click or Scroll")
    st.write("Move: Control + Left Click")
    st.write("Use the dropdown menu to change the molecular representation.")
    st.write("Check the box to include hydrogen atoms in the visualization.")
