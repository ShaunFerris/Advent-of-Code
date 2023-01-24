from module import buffer_scan, buffer_scan_message

file = open('input.txt')
buffer = file.read()
print(buffer_scan(buffer))
print(buffer_scan_message(buffer))