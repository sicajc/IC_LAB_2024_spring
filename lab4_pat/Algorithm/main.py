from CNN import CNN
from CNN_pattern_gen import CNN_pattern_gen

def main():
  PAT_NUM = 1000
  PAT_GEN = False
  PAT_TO_DEBUG = 3
  DEBUG   = False

  in_file_dir = './Verilog/input.txt'
  out_file_dir = './Verilog/output.txt'
  debug_log_dir = './Algorithm/debug.log'

  if PAT_GEN == True:
    CNN_pattern_gen(PAT_NUM, in_file_dir)

  CNN(PAT_NUM=PAT_TO_DEBUG,
      DEBUG=DEBUG,
      in_file_dir=in_file_dir,
      out_file_dir=out_file_dir,
      debug_log_dir=debug_log_dir)

  print("Done!")
  return

if __name__ == "__main__":
    main()