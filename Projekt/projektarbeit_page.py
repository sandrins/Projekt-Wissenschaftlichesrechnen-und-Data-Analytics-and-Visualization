import streamlit as st

st.title("Projektarbeit Wissenschaftliches Rechnen")

'''
Auf dieser Seite kann die Projektarbeit aus dem Fach Wissenschaftliches Rechnen heruntergeladen werden.
'''

zip_file_name = "Projektarbeit_Wissenschaftliches_Rechnen_Andrin_Sutter.zip"
file_path = "Projekt\Projektarbeit_Wissenschaftliches_Rechnen_Andrin_Sutter.zip"

st.subheader("Download Projektarbeit")

st.write("Klicken Sie auf den Button, um die Projektarbeit als ZIP-Datei herunterzuladen:")

# Read the file
with open(file_path, "rb") as file:
    content = file.read()
# Download Button
st.download_button(
    label="📁 Download Projektarbeit",
    data=content,
    file_name=zip_file_name,
    mime="application/zip"
    )