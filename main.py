from docling.document_converter import DocumentConverter
from pathlib import Path


def pdf_to_markdown(pdf_path: str, output_path: str):
    # Initialize Docling converter
    converter = DocumentConverter()

    # Convert the PDF
    result = converter.convert(pdf_path)

    # Extract Markdown
    markdown = result.document.export_to_markdown()

    # Save to file
    Path(output_path).write_text(markdown, encoding="utf-8")
    print(f"✅ Converted {pdf_path} -> {output_path}")


if __name__ == "__main__":
    pdf_to_markdown("sample.pdf", "output.md")
