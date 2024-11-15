def optimal_page_replacement(pages, frame_size):
    frame = []  # List to store pages in frame
    page_faults = 0  # Count page faults

    for i, page in enumerate(pages):
        if page not in frame:
            if len(frame) < frame_size:
                # Add page if there is space in the frame
                frame.append(page)
            else:
                # Find the page in the frame that will not be used for the longest time in future
                future_uses = []
                for f_page in frame:
                    if f_page in pages[i + 1:]:
                        # Find next occurrence of each page in the frame
                        next_use = pages[i + 1:].index(f_page)
                    else:
                        # If a page is not going to be used again, choose it for replacement
                        next_use = float('inf')
                    future_uses.append(next_use)

                # Replace the page with the farthest future use
                frame.pop(future_uses.index(max(future_uses)))
                frame.append(page)
            
            page_faults += 1
            print(f"Page {page} caused a page fault. Frame: {frame}")
        else:
            print(f"Page {page} is already in frame. Frame: {frame}")

    print(f"\nTotal Page Faults: {page_faults}")

# Example usage
pages = [1, 3, 0, 3, 5, 6, 3]
frame_size = 3
optimal_page_replacement(pages, frame_size)
