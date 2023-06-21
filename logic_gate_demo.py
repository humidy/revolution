"""
描述：这是一个利用Python类的特性测试逻辑门的程序，实现各种逻辑门的定义和组合
作者：humidy
时间：2023-06
注：本程序首次使用了Python的Pylint进展规范性检测，编码规范通过Pylint测试
"""
# -*- coding:utf-8 -*-
import sys


# 定义一个逻辑门通用操作，提供最基础的功能
class LogicGate:
    """
    定义一个最基础的逻辑门单元，包含通用属性（名称、类型、输出等）
    """

    def __init__(self, n):
        # 定义逻辑门的名称
        self.label = n
        # 定义逻辑门的类型
        self.type = '未定义'
        # 定义逻辑门的输出（假设每一个逻辑门都有输出）
        self.output = None

    # 获取逻辑门的名称
    def get_label(self):
        """
        :return:返回逻辑门的标签名称
        """
        return self.label

    # 获取逻辑门的类型
    def get_type(self):
        """
        :return: 输出逻辑门的类型
        """
        return self.type

    # 获取逻辑门的输出
    def get_output(self):
        """
        :return:返回逻辑门的输出值（这里假设逻辑门都只有一个输出）
        """
        return self.output


# 检查输入值的有效性，输入值为数值，且取值为0或1
def check_input_format(input_name=None, gate=LogicGate(None)):
    """
    :param input_name: 输入端的名称，对于输入>1的，有几个输入就会有几个输入名（用单个大写字母表示），对于输入=1的默认名字为None
    :param gate:
    :return:
    """
    try:
        # 判断输入的类型
        if input_name:
            input_value = int(input("[正常]：逻辑门[{}]的输入_{}："
                                    .format(gate.label, input_name)))
        else:
            input_value = int(input("[正常]：逻辑门[{}]的输入："
                                    .format(gate.label)))
    # 输入值转换错误
    except ValueError:
        print("[错误]：类型错误，输入类型不合法,输入类型为数值型且数值为0或1")
        sys.exit()
    # 其它未知错误
    except Exception as err:
        print("[错误]：出现未知错误，错误原因{}".format(err))
        sys.exit()
    # 判断输入的值
    if input_value in (0, 1):
        return input_value
    print("[错误]：值错误，输入值不合法，输入值为0或1")
    sys.exit()


# 定义含有两个输入的逻辑门
class BinaryGate(LogicGate):
    """
    pass
    """

    def __init__(self, n):
        super().__init__(n)
        # 定义逻辑门的两个输入值和名称，名称默认为1和2
        self.input_1_value = None
        self.input_2_value = None
        self.input_1_name = '1'
        self.input_2_name = '2'

    # 处理逻辑门的输入值1
    def process_input_1(self):
        """
        :return:判断输入值一是否为空（有值），如果为空则可以赋值
        """
        if self.input_1_value is None:
            self.input_1_value = check_input_format(self.input_1_name, self)
        else:
            print("[异常]：无法输入，逻辑门[{}]的输入[{}]已有值，值为[{}]"
                  .format(self.label, self.input_1_name, self.input_1_value))

    # 处理逻辑门的输入值2
    def process_input_2(self):
        """
        :return:
        """
        if self.input_2_value is None:
            self.input_2_value = check_input_format(self.input_2_name, self)
        else:
            print("[异常]：无法输入，逻辑门[{}]的输入[{}]已有值，值为[{}]"
                  .format(self.label, self.input_2_name, self.input_2_value))

    # 获取输入1的值
    def get_input_1_value(self):
        """
        :return:
        """
        return self.input_1_value

    # 获取输入2的值
    def get_input_2_value(self):
        """
        :return:
        """
        return self.input_2_value

    # 获取输入1的名字
    def get_input_1_name(self):
        """
        :return:
        """
        return self.input_1_name

    # 获取输入2的名称
    def get_input_2_name(self):
        """
        :return:
        """
        return self.input_2_name


# 定义含有一个输入的逻辑门
class UnaryGate(LogicGate):
    """
    pass
    """

    def __init__(self, n):
        super().__init__(n)
        self.input_value = None
        self.input_name = None

    # 获取输入的值
    def process_input(self):
        """
        :return:
        """
        if self.input_value is None:
            self.input_value = check_input_format(self.input_name, self)
        else:
            print("[异常]：无法输入，逻辑门[{}]的输入已有值，值为[{}]"
                  .format(self.label, self.input_value))

    # 获取输入的值
    def get_input_value(self):
        """
        :return:
        """
        return self.input_value

    # 获取输入的名字
    def get_input_name(self):
        """
        :return:
        """
        return self.input_name


# 定义"与"逻辑门的操作
class AndGate(BinaryGate):
    """
    pass
    """

    def __init__(self, n):
        super().__init__(n)
        # 定义逻辑门的类型
        self.type = "与门"
        print("[信息]：逻辑门[{}]是[{}]".format(self.label, self.type))

    # "与"的判断逻辑
    def perform_gate_logic(self):
        """
        :return:
        """
        self.process_input_1()
        self.process_input_2()
        # 两个值的"与"操作结果（这里用朴素的值运算实现）
        if self.input_1_value == 1 and self.input_2_value == 1:
            self.output = 1
        else:
            self.output = 0


# 定义或逻辑门的操作
class OrGate(BinaryGate):
    """
    pass
    """

    def __init__(self, n):
        super().__init__(n)
        # 定义逻辑门的类型
        self.type = "或门"
        # 输出描述信息
        print("[信息]：逻辑门[{}]是[{}]".format(self.label, self.type))

    # "或"的判断逻辑
    def perform_gate_logic(self):
        """
        :return:
        """
        self.process_input_1()
        self.process_input_2()
        # 两个值的"或"操作结果（这里用朴素的值运算实现）
        if self.input_1_value == 0 and self.input_2_value == 0:
            self.output = 0
        else:
            self.output = 1


# 定义"非"的逻辑门操作
class NotGate(UnaryGate):
    """
    pass
    """

    def __init__(self, n):
        super().__init__(n)
        self.type = "非门"
        # 输出描述信息
        print("[信息]：逻辑门[{}]是[{}]".format(self.label, self.type))

    # "非"的判断逻辑
    def perform_gate_logic(self):
        """
        :return:
        """
        self.process_input()
        # 一个值的"非"操作结果（这里用朴素的值运算实现）
        if self.input_value == 0:
            self.output = 1
        else:
            self.output = 0


# 定义"异或"逻辑门的操作
class XorGate(BinaryGate):
    """
    pass
    """

    def __init__(self, n):
        super().__init__(n)
        self.type = "异或门"
        # 输出描述信息
        print("[信息]：逻辑门[{}]是[{}]".format(self.label, self.type))

    # 重写"异或"判断逻辑
    def perform_gate_logic(self):
        """
        :return:
        """
        self.process_input_1()
        self.process_input_2()
        # 两个值的"异或"操作结果（这里用朴素的值运算实现）
        if self.input_1_value == self.input_2_value:
            self.output = 0
        else:
            self.output = 1


# 定义"与非"逻辑门的操作
class NotAndGate(BinaryGate):
    """
    pass
    """

    def __init__(self, n):
        super().__init__(n)
        self.type = "与非门"
        # 输出描述信息
        print("[信息]：逻辑门[{}]是[{}]".format(self.label, self.type))

    # 重写"与非"判断逻辑
    def perform_gate_logic(self):
        """
        :return:
        """
        self.process_input_1()
        self.process_input_2()
        # 两个值的"与非"操作结果（这里用朴素的值运算实现）
        if self.input_1_value == 1 and self.input_2_value == 1:
            self.output = 0
        else:
            self.output = 1


# 定义"或非"逻辑门的操作
class NotOrGate(BinaryGate):
    """
    pass
    """

    def __init__(self, n):
        super().__init__(n)
        self.type = "或非门"
        # 输出描述信息
        print("[信息]：逻辑门[{}]是[{}]".format(self.label, self.type))

    # 重写"或非"判断逻辑
    def perform_gate_logic(self):
        """
        :return:
        """
        self.process_input_1()
        self.process_input_2()
        # 两个值的"或非"操作结果（这里用朴素的值运算实现）
        if self.input_1_value == 0 and self.input_2_value == 0:
            self.output = 1
        else:
            self.output = 0


# 定义门与门的连接器,执行连接过程
class GateConnection:
    """
    定义门的连接操作，这里假设2个门都是符合规范的门实例，未进行门的有效性判断
    """

    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate
        # 输出连接信息
        print("开始连接，从逻辑门[{}]到逻辑门[{}]"
              .format(from_gate.label, to_gate.label))

    def connection(self):
        """
        :return:
        """
        # 根据门的类型定义输入，输出的情况（两个输入）
        if isinstance(self.to_gate, BinaryGate):
            # 判断接受输入门的A口是否有空
            if self.to_gate.input_1_value is None:
                self.from_gate.perform_gate_logic()
                self.to_gate.input_1_value = self.from_gate.output
            # 判断接受输入门的B口是否有空
            elif self.to_gate.input_b is None:
                self.from_gate.perform_gate_logic()
                self.to_gate.input_b = self.from_gate.output
            else:
                print("[异常]逻辑门{}的输入口已满，无法接入新的输入".format(self.to_gate.label))
        # 根据门的类型定义输入，输出的情况（一个输入）
        else:
            if self.to_gate.input is None:
                self.from_gate.perform_gate_logic()
                self.to_gate.input = self.from_gate.output

    def get_from_gate(self):
        """
        :return:
        """
        return self.from_gate

    def get_to_gate(self):
        """
        :return:
        """
        return self.to_gate


# 获取逻辑门的相关信息
class GetGateInfo:
    """
    输出逻辑门当前的信息包含一些基本属性（名称、类型）、输入和输出等
    """

    def __init__(self, gate_ins):
        self.gate_ins = gate_ins

    def print_detail(self):
        """
        :return:
        """
        print("=" * 52)
        # 有两个输入的情况
        if isinstance(self.gate_ins, BinaryGate):
            print("[信息]:逻辑门[{}]是[{}],有2个输入和1个输出如下:"
                  .format(self.gate_ins.label, self.gate_ins.type))
            print("[信息]:逻辑门[{}]的输入_{}：[{}]"
                  .format(self.gate_ins.label, self.gate_ins.input_1_name, self.gate_ins.input_1_value))
            print("[信息]:逻辑门[{}]的输入_{}：[{}]"
                  .format(self.gate_ins.label, self.gate_ins.input_2_name, self.gate_ins.input_2_value))
            print("[信息]:逻辑门[{}]的输出：[{}]"
                  .format(self.gate_ins.label, str(self.gate_ins.output)))
        # 有一个输入的情况
        else:
            print("[信息]:逻辑门[{}]是[{}],有1个输入和1个输出如下:"
                  .format(self.gate_ins.label, self.gate_ins.type))
            print("[信息]:逻辑门[{}]的输入：[{}]"
                  .format(self.gate_ins.label, self.gate_ins.input_value))
            print("[信息]:逻辑门[{}]的输出：[{}]"
                  .format(self.gate_ins.label, self.gate_ins.output))
        print("=" * 52)

    def get_gate_ins(self):
        """
        :return:
        """
        return self.gate_ins


if __name__ == "__main__":
    # g1 = AndGate('g1')
    # g2 = OrGate('g2')
    # g3 = XorGate('g3')
    # g4 = NotGate('g4')
    #
    # print("============================================")
    #
    # GateConnection(g1, g3).connection()
    # GetGateInfo(g1).print_detail()
    #
    # GateConnection(g2, g3).connection()
    # GetGateInfo(g2).print_detail()
    #
    # GateConnection(g3, g4).connection()
    # GetGateInfo(g3).print_detail()
    #
    # g4.perform_gate_logic()
    # GetGateInfo(g4).print_detail()

    g1 = NotAndGate('g1')
    g1.perform_gate_logic()
    GetGateInfo(g1).print_detail()
