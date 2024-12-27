import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from ultralytics import YOLO
import time

MODEL_PATH = "best_modelSDG100.pt" 

# Load model
model = YOLO(MODEL_PATH)

# Streamlit UI
st.title("Deteksi Buah: Segar atau Busuk dengan YOLOv11")
st.write("Upload gambar untuk mendeteksi dan mengklasifikasi buah.")

# Warna hasil prediksi sama dengan warna area upload
RESULT_BOX_STYLE = "color: white; background-color: #4CAF50; padding: 10px; border-radius: 5px;"

uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "png", "jpeg"])

# Simpan state gambar yang diunggah
if 'image' not in st.session_state:
    st.session_state['image'] = None

if uploaded_file is not None:
    # Buka gambar
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diunggah")

    # Gambar dengan transparansi (RGBA)
    if image.mode == "RGBA":
        image = image.convert("RGB")  # Konversi ke RGB

    # Simpan gambar ke state untuk prediksi
    st.session_state['image'] = image

# Button prediksi
if st.session_state['image'] is not None and st.button("Mulai Prediksi"):
    with st.spinner("Memproses gambar, mohon tunggu..."):
        time.sleep(2)  

        # Menyimpan gambar untuk di prediksi 
        temp_image_path = "temp_uploaded_image.jpg"
        st.session_state['image'].save(temp_image_path, format="JPEG")

        # Prediksi dengan YOLOv11
        results = model(temp_image_path)

        # Menampilkan hasil deteksi
        st.write("Hasil Deteksi:")
        original_image = st.session_state['image'].copy()
        draw = ImageDraw.Draw(original_image)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                label = result.names[int(box.cls)]
                confidence = float(box.conf)

                # Bounding box ke gambar
                draw.rectangle([x1, y1, x2, y2], outline="red", width=3)

                # Menambahkan label dan confidence
                text = f"{label} {confidence:.2%}"
                draw.text((x1, y1 - 10), text, fill="red")

                st.markdown(f"<div style='{RESULT_BOX_STYLE}'>Label: {label}, Confidence: {confidence:.2%}</div>", unsafe_allow_html=True)

        # Menampilkan gambar dengan bounding box
        st.image(original_image, caption="Gambar dengan Bounding Box")
