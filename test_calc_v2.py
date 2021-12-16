import calc_v2, pytest
#считывание числа
@pytest.mark.parametrize("num_str, num",[('123', 123), ('1000000000', 1000000000),
                                         ('-42341450', -42341450)])
def test_read_number_pos(num_str, num):
      assert calc_v2.read_number(num_str) == num

@pytest.mark.parametrize("num_str, num",[('a12с', ""), ('10000000000', 10000000000),
                                         ('3214-3', "3214-3"), ('13,3', 13.3), ('0xbd1', "")])
def test_read_number_neg(num_str, num):
      with pytest.raises(Exception):
            calc_v2.read_number(num_str) == num
#------------------------------------------------

#считывание действия
@pytest.mark.parametrize("op_to_test, result_op", [('+', '+'), ('*', '*'), ('-', '-'),
                                                   ('/', '/'), ('**', '**')])
def test_read_operation_pos(op_to_test, result_op):
      assert calc_v2.read_operation(op_to_test) == result_op

@pytest.mark.parametrize("op_to_test, result_op", [('a', 'a'), ('//', '//'), ('+-', '+-')])
def test_read_operation_neg(op_to_test, result_op):
      with pytest.raises(Exception):
            calc_v2.read_operation(op_to_test) == result_op
#------------------------------------------------
      
#вычисление результата
@pytest.mark.parametrize("first_num, second_num, operation, result", [(5, 5, '+', 'a'),
                                                                      (43, 32, '*', '560')])
def test_perform_operation_pos(first_num, second_num, operation, result):
      assert calc_v2.perform_operation(first_num, second_num, operation) == result

@pytest.mark.parametrize("first_num, second_num, operation, result", [(5, 0, '/', "fail"),
                                                                      (5555, 5555, '**', "fail")])
def test_perform_operation_neg(first_num, second_num, operation, result):
      with pytest.raises(Exception):
            calc_v2.perform_operation(first_num, second_num, operation) == result
