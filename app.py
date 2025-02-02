from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_bmi(weight, height):
    """计算BMI指数"""
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None


def get_bmi_status(bmi, sex):
    """根据BMI指数和性别获取健康状态"""
    if bmi is None:
        return "身高不能为零"
    elif sex == "男":
        if bmi < 18.5:
            return "体重过轻"
        elif 18.5 <= bmi < 24.9:
            return "正常范围"
        else:
            return "超重"
    elif sex == "女":
        if bmi < 18.5:
            return "体重过轻"
        elif 18.5 <= bmi < 23.9:
            return "正常范围"
        else:
            return "超重"


@app.route('/', methods=['GET'])
def index():
    """显示BMI计算表单页面"""
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    """处理表单提交，计算BMI并显示结果"""
    sex = request.form.get('sex')
    try:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calculate_bmi(weight, height)
        status = get_bmi_status(bmi, sex)
        # 将身高和体重传递给模板
        return render_template('result.html', bmi=bmi, status=status, sex=sex, height=height, weight=weight)
    except (ValueError, TypeError):
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)