import file_operations as file

if __name__ == '__main__':
    file.create_file_w_mode("Hello file!\nBye file!")
    file.create_file_r_mode()
    file.create_file_a_mode("\nNew line/life baby!")
    file.create_file_r_mode()
    file.read_file_with_loop()
