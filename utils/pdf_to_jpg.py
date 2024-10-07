from pdf2image import convert_from_path
import os
def pdf_to_jpg(pdf_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF to images
    images = convert_from_path(pdf_path)

    jpg_files = []
    # Save each page as a JPEG file
    for i, image in enumerate(images):
        file_name = os.path.basename(pdf_path).replace('.pdf', '')
        
        if i == 0:
            # Single page
            image_path = os.path.join(output_folder, f'{file_name}.jpg')
        else:
            # Multiple pages
            image_path = os.path.join(output_folder, f'{file_name}_page_{i+1}.jpg')
        
        image.save(image_path, 'JPEG')
        jpg_files.append(image_path)

    return jpg_files
