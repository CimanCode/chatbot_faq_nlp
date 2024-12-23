# chatbot/management/commands/seed_faq.py
from django.core.management.base import BaseCommand
from chatbot_rule_based.models import FAQ

class Command(BaseCommand):
    help = 'Menambahkan data FAQ ke dalam database'

    def handle(self, *args, **kwargs):
        faq_data = [
            {"question": "Apa itu HTML?", "answer": "HTML adalah bahasa markup standar untuk membuat struktur halaman web."},
            {"question": "Apa itu CSS?", "answer": "CSS adalah bahasa yang digunakan untuk mengatur tampilan dan tata letak halaman web."},
            {"question": "Apa itu JavaScript?", "answer": "JavaScript adalah bahasa pemrograman untuk halaman web interaktif."},
            {"question": "Apa itu framework web?", "answer": "Framework web adalah kerangka kerja untuk mempermudah pengembangan aplikasi web."},
            {"question": "Apa perbedaan frontend dan backend?", "answer": "Frontend adalah bagian yang terlihat oleh pengguna, backend adalah bagian yang menangani logika dan database."},
            # Tambahkan data FAQ lainnya sesuai kebutuhan
        ]

        for item in faq_data:
            FAQ.objects.create(question=item["question"], answer=item["answer"])

        self.stdout.write(self.style.SUCCESS('FAQ data berhasil ditambahkan'))
