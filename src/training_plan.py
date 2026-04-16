def model(x, w):
    return x * w

def loss(y, y_pred):
    return (y - y_pred) ** 2

def gradient(x, w, y_true):
    y_pred = model(x, w)
    grad = 2 * (y_pred - y_true) * x
    return grad

# def train():
w = 1.0  # Initial weight
x = 2.0  # Input
y_true = 10  # True output
learning_rate = 0.01

for epoch in range(100):
    y_pred = model(x, w)
    current_loss = loss(y_true, y_pred)
    grad = gradient(x, w, y_true)
    
    w -= learning_rate * grad  # Update weight
    
    if epoch % 10 == 0:
        print(f'Epoch {epoch}: Loss={current_loss:.4f}, Weight={w:.4f}')