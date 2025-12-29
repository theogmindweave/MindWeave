#!/usr/bin/env python3
"""
HTML to Markdown Converter for Competitor Documentation
Converts HTML clones to structured markdown files for analysis
"""

import os
import sys
from pathlib import Path
from html.parser import HTMLParser
import re
from datetime import datetime

class HTMLToMarkdownConverter(HTMLParser):
    """Convert HTML content to clean markdown"""

    def __init__(self):
        super().__init__()
        self.reset()
        self.text_parts = []
        self.in_script = False
        self.in_style = False
        self.in_meta = False
        self.heading_level = 0
        self.list_items = []
        self.in_list = False
        self.current_list_type = None
        self.image_refs = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == 'script':
            self.in_script = True
        elif tag == 'style':
            self.in_style = True
        elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            self.heading_level = level
        elif tag == 'p':
            pass
        elif tag == 'br':
            self.text_parts.append('\n')
        elif tag == 'img':
            alt = attrs_dict.get('alt', 'image')
            src = attrs_dict.get('src', '#')
            self.image_refs.append({'src': src, 'alt': alt})
        elif tag in ['ul', 'ol']:
            self.in_list = True
            self.current_list_type = 'ul' if tag == 'ul' else 'ol'
            self.list_items = []
        elif tag == 'li':
            pass
        elif tag == 'a':
            href = attrs_dict.get('href', '#')
            pass
        elif tag == 'strong' or tag == 'b':
            self.text_parts.append('**')
        elif tag == 'em' or tag == 'i':
            self.text_parts.append('*')
        elif tag == 'code':
            self.text_parts.append('`')

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = False
        elif tag == 'style':
            self.in_style = False
        elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            if self.text_parts and self.heading_level > 0:
                content = ''.join(self.text_parts).strip()
                if content:
                    self.text_parts = ['#' * self.heading_level + ' ' + content + '\n\n']
            self.heading_level = 0
        elif tag == 'p':
            if self.text_parts:
                self.text_parts.append('\n\n')
        elif tag in ['ul', 'ol']:
            self.in_list = False
            if self.list_items:
                for item in self.list_items:
                    self.text_parts.append(item + '\n')
                self.text_parts.append('\n')
            self.current_list_type = None
            self.list_items = []
        elif tag == 'li':
            if self.text_parts:
                item_text = ''.join(self.text_parts).strip()
                prefix = '- ' if self.current_list_type == 'ul' else '1. '
                self.list_items.append(prefix + item_text)
                self.text_parts = []
        elif tag == 'a':
            pass
        elif tag == 'strong' or tag == 'b':
            self.text_parts.append('**')
        elif tag == 'em' or tag == 'i':
            self.text_parts.append('*')
        elif tag == 'code':
            self.text_parts.append('`')

    def handle_data(self, data):
        if not self.in_script and not self.in_style:
            text = data.strip()
            if text and not text.startswith('<!'):
                self.text_parts.append(text)

    def get_text(self):
        content = ''.join(self.text_parts)
        # Clean up multiple newlines
        content = re.sub(r'\n{3,}', '\n\n', content)
        # Remove common noise
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        return content.strip()

def extract_title_from_html(html_content):
    """Extract title from HTML"""
    match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "Untitled"

def extract_meta_description(html_content):
    """Extract meta description from HTML"""
    match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html_content, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""

def convert_html_file_to_md(html_path, output_path):
    """Convert a single HTML file to markdown"""
    try:
        with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()

        title = extract_title_from_html(html_content)
        description = extract_meta_description(html_content)

        # Extract body content only
        body_match = re.search(r'<body[^>]*>(.*)</body>', html_content, re.DOTALL | re.IGNORECASE)
        body_content = body_match.group(1) if body_match else html_content

        # Remove navigation and footer patterns
        body_content = re.sub(r'<nav[^>]*>.*?</nav>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
        body_content = re.sub(r'<footer[^>]*>.*?</footer>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
        body_content = re.sub(r'<header[^>]*>.*?</header>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
        body_content = re.sub(r'class="[^"]*"', '', body_content)
        body_content = re.sub(r'id="[^"]*"', '', body_content)

        # Convert HTML to text
        converter = HTMLToMarkdownConverter()
        converter.feed(body_content)
        text_content = converter.get_text()

        # Build markdown
        md_content = f"# {title}\n\n"
        if description:
            md_content += f"> {description}\n\n"
        md_content += text_content

        # Write markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        return True, len(md_content)
    except Exception as e:
        return False, str(e)

def process_directory(source_dir, output_dir, platform_name):
    """Process all HTML files in a directory"""
    print(f"\n{'='*60}")
    print(f"Processing {platform_name}")
    print(f"Source: {source_dir}")
    print(f"Output: {output_dir}")
    print(f"{'='*60}\n")

    converted = []
    failed = []

    source_path = Path(source_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for html_file in sorted(source_path.glob('*.html')):
        relative_name = html_file.name
        md_name = html_file.stem + '.md'

        output_file = output_path / md_name

        success, info = convert_html_file_to_md(str(html_file), str(output_file))

        if success:
            converted.append((relative_name, md_name, info))
            print(f"✓ {relative_name} → {md_name}")
        else:
            failed.append((relative_name, info))
            print(f"✗ {relative_name}: {info}")

    # Process subdirectories
    for subdir in source_path.iterdir():
        if subdir.is_dir() and subdir.name not in ['assets', 'common', 'cdn-cgi', '_next', 'static']:
            sub_output = output_path / subdir.name
            sub_output.mkdir(parents=True, exist_ok=True)

            for html_file in sorted(subdir.glob('*.html')):
                relative_name = f"{subdir.name}/{html_file.name}"
                md_name = html_file.stem + '.md'

                output_file = sub_output / md_name

                success, info = convert_html_file_to_md(str(html_file), str(output_file))

                if success:
                    converted.append((relative_name, f"{subdir.name}/{md_name}", info))
                    print(f"✓ {relative_name} → {subdir.name}/{md_name}")
                else:
                    failed.append((relative_name, info))
                    print(f"✗ {relative_name}: {info}")

    print(f"\n{'='*60}")
    print(f"Summary for {platform_name}:")
    print(f"Converted: {len(converted)} files")
    print(f"Failed: {len(failed)} files")
    print(f"{'='*60}\n")

    return converted, failed

def main():
    base_path = "/Users/vijaygorfad/Desktop/MindWeave/TheOGMindWeave/01-research"
    output_base = f"{base_path}/competitor-docs"

    results = {}

    # Process Adadot
    adadot_converted, adadot_failed = process_directory(
        f"{base_path}/adadot-clone",
        f"{output_base}/adadot",
        "Adadot Clone"
    )
    results['adadot'] = {'converted': len(adadot_converted), 'failed': len(adadot_failed)}

    # Process Workweave
    workweave_converted, workweave_failed = process_directory(
        f"{base_path}/workweave-clone",
        f"{output_base}/workweave",
        "Workweave Clone"
    )
    results['workweave'] = {'converted': len(workweave_converted), 'failed': len(workweave_failed)}

    # Process Hunted Space
    hunted_converted, hunted_failed = process_directory(
        f"{base_path}/hunted-space-clone",
        f"{output_base}/hunted-space",
        "Hunted Space Clone"
    )
    results['hunted-space'] = {'converted': len(hunted_converted), 'failed': len(hunted_failed)}

    # Print final summary
    print(f"\n{'='*60}")
    print("FINAL SUMMARY")
    print(f"{'='*60}")
    total_converted = sum(r['converted'] for r in results.values())
    total_failed = sum(r['failed'] for r in results.values())

    for platform, counts in results.items():
        print(f"{platform.upper()}: {counts['converted']} converted, {counts['failed']} failed")

    print(f"\nTOTAL: {total_converted} converted, {total_failed} failed")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
