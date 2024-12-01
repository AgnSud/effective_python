import argparse

parser = argparse.ArgumentParser(description='COmputing Newtons method')
parser.add_argument('--f', type=str, required=True, help='function')
parser.add_argument('--x0', type=float, required=True, help='initial point for method')
parser.add_argument('--d_step', type=float, default=1, help='step of derivative')
parser.add_argument('--steps', type=float, default=10, help='number of steps')
parser.add_argument('--a', type=float, default=0.0001, help='accuracy of method')
parser.add_argument('--help_extended', action="help", help='for more info check wiki')


def evaluate_function(expression, x):
    try:
        return eval(expression)
    except Exception as e:
        raise ValueError(f"Error while computing {x}: {e}")
def newtons_method():
    '''
    Przygotuj demo programu znajdującego miejsca zerowe metodą Newtona. Wykorzystując `argparse` ([link](https://docs.python.org/3.6/library/argparse.html#module-argparse)) lub `optparse` ([link](https://docs.python.org/3.6/library/optparse.html)) obsłuż:
    - ustalane punktu startowego,
    - wielkość kroku w pochodnej,
    - ilość kroków metody,
    - dokładność
    - pomoc

    Program uruchamiamy podając, np.:
    `./newton.py x**2+x+1 -h 0.00001`
    '''
    args = parser.parse_args()
    x = args.x0
    for i in range(args.steps):
        f_x = evaluate_function(args.f, x)
        f_x_plus_h = evaluate_function(args.f, x + args.d_step)
        derivative = (f_x_plus_h - f_x) / args.d_step
        x = x - f_x / derivative
        if abs(f_x) < args.a:
            break
    return x


print(newtons_method())