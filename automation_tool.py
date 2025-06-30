import os
import shutil
import re
import requests

def move_jpg_files():
    source_folder = 'C:/Users/srija/Downloads'
    destination_folder = 'C:/Users/srija/Pictures/JPGs'
    os.makedirs(destination_folder, exist_ok=True)

    jpg_files_moved = 0
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith('.jpg'):
            source_path = os.path.join(source_folder, file_name)
            dest_path = os.path.join(destination_folder, file_name)

            # Handle filename conflicts
            if os.path.exists(dest_path):
                base, ext = os.path.splitext(file_name)
                counter = 1
                while os.path.exists(dest_path):
                    new_name = f"{base}_{counter}{ext}"
                    dest_path = os.path.join(destination_folder, new_name)
                    counter += 1

            shutil.move(source_path, dest_path)
            print(f"Moved: {file_name} → {os.path.basename(dest_path)}")
            jpg_files_moved += 1

    print(f"\n✅ Total JPG files moved: {jpg_files_moved}")

def extract_emails():
    input_file = 'sample.txt'
    output_file = 'extracted_emails.txt'

    if not os.path.exists(input_file):
        print(f"⚠️ File '{input_file}' not found.")
        return

    with open(input_file, 'r') as file:
        text = file.read()

    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')

    print(f"\n✅ {len(emails)} email(s) extracted and saved to '{output_file}'")

def scrape_webpage_title():
    url = input("Enter the URL of the webpage (e.g., https://example.com): ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
            if match:
                title = match.group(1)
                with open('webpage_title.txt', 'w') as f:
                    f.write(title)
                print(f"\n✅ Webpage title saved: {title}")
            else:
                print("⚠️ Could not find <title> tag in the webpage.")
        else:
            print(f"❌ Failed to fetch webpage. Status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error occurred: {e}")

def main():
    print("\n🔧 Task Automation Tool with Python")
    print("----------------------------------")
    print("1. Move .jpg files")
    print("2. Extract emails from .txt")
    print("3. Scrape title from a webpage")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        move_jpg_files()
    elif choice == '2':
        extract_emails()
    elif choice == '3':
        scrape_webpage_title()
    elif choice == '4':
        print("👋 Exiting program.")
    else:
        print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
