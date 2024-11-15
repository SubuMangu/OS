def mru_page_replacement(pages, frame_size):
    frame = []  # List to store pages in frame
    page_faults = 0  # Count page faults

    for page in pages:
        if page not in frame:
            # If page is not in frame and frame has space, add page
            if len(frame) < frame_size:
                frame.append(page)
            else:
                # If frame is full, remove the most recently used page
                frame.pop(-1)
                frame.append(page)
            page_faults += 1
            print(f"Page {page} caused a page fault. Frame: {frame}")
        else:
            # If page is in frame, mark it as most recently used by moving it to the end
            frame.remove(page)
            frame.append(page)
            print(f"Page {page} is already in frame. Frame: {frame}")

    print(f"\nTotal Page Faults: {page_faults}")

# Example usage
pages = [1, 3, 0, 3, 5, 6, 3]
frame_size = 3
mru_page_replacement(pages, frame_size)
