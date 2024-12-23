# Chatbot FAQ dengan Django, SVM, dan TF-IDF

Proyek ini adalah **Chatbot FAQ berbasis aturan (Rule-Based Chatbot)** yang dibangun menggunakan framework **Django**. Chatbot ini menggunakan algoritma **SVM (Support Vector Machine)** dan **TF-IDF (Term Frequency-Inverse Document Frequency)** untuk memproses pertanyaan dan memberikan jawaban yang relevan. Chatbot ini dirancang untuk menjawab pertanyaan yang sering diajukan (FAQ) terkait suatu domain tertentu.

---

## Fitur Utama
- **Chatbot FAQ**: Menjawab pertanyaan dari pengguna berdasarkan data FAQ yang telah didefinisikan sebelumnya.
- **TF-IDF**: Mengubah teks pertanyaan menjadi bentuk numerik untuk diproses.
- **SVM**: Memprediksi jawaban paling relevan untuk pertanyaan yang diajukan.
- **Antarmuka Web**: Tersedia antarmuka web yang menarik dan responsif.
- **Penyimpanan MySQL**: Data FAQ disimpan di database MySQL.

---

## Teknologi yang Digunakan
- **Backend**:
  - Python (v3.x)
  - Django (v4.x)
  - scikit-learn (untuk TF-IDF dan SVM)
- **Frontend**:
  - HTML/CSS/JavaScript
  - Bootstrap (untuk desain responsif)
- **Database**:
  - MySQL
- **Lainnya**:
  - Git (untuk kontrol versi)

---

## Cara Menggunakan Aplikasi

### **Persyaratan Sistem**
Sebelum memulai, pastikan Anda telah menginstal:
1. **Python** (versi 3.x)
2. **MySQL** (untuk menyimpan data FAQ)
3. **pip** (pengelola paket Python)
4. **Git** (opsional, untuk mengunduh repositori)

---

### **Langkah-langkah Instalasi**

#### **1. Clone Repositori**
Unduh proyek dari GitHub ke komputer Anda:
```bash
git clone https://github.com/username/chatbot-faq-django.git
cd chatbot-faq-django
python -m venv env
source env/bin/activate  # Untuk Windows: venv\Scripts\activate
python manage.py runserver

