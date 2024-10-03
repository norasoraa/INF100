def rotate_string(s,k):
   første_del = s[:k % len(s)]
   andre_del = s[k % len(s):]
   return andre_del + første_del

print(rotate_string("Hello World!", 5))