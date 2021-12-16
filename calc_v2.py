
def read_number(x: str) -> int:
      
      x = int(x)
      assert len(str(abs(x))) <= 10, "Разрядность введенного числа превышает допустимую"  #проверка разрядности 
      return x

def read_operation(op) -> str:
     
      assert op in ("+", "-", "*", "/", "**"), "Введена некорректная операция"
      
      return op

def perform_operation(first_num, second_num, operation):
      #print(first_num, operation, second_num)
      if operation == "+":
            result = first_num + second_num
      elif operation == "-":
            result = first_num - second_num
      elif operation == "*":
            result = first_num * second_num
      elif operation == "/":
            result = first_num / second_num
      elif operation == "**":
            result = first_num ** second_num

      check_len = str(hex(abs(int(result))))[2:]
      
      result = hex(int(result))
      #print(result)

      assert len(check_len) <= 9, "Разрядность результирующего числа превышает допустимую"
      #print("\nРезультат выводится в шестнадцатеричной системе исчисления")
      #print(first_num, operation, second_num, "=", str(result)[2:])
      return str(result)[2:]
     

      


if __name__ == "__main__":
      x = input("\nВведите первое число (десятичное, до 10 разрядности включительно): ")
      first_num = read_number(x)
      #print(first_num)
      x = input("\nВведите второе число (десятичное, до 10 разрядности включительно): ")
      second_num = read_number(x)
      #print(second_num)
      op = input("\nВведите операцию ((+, -, *, /, **): ")
      operation = read_operation(op)
      #print(operation)
      print("\nРезультат выводится в шестнадцатеричной системе исчисления ")
      #print(first_num, operation, second_num, "=", str(result)[2:])
      print(first_num, operation, second_num, "=", perform_operation(first_num, second_num, operation))
      input()

      
