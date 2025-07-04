def split_and_join(line):
  words=line.split()
  join="-".join(words)
  return join
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
