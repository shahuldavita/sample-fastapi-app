```javascript
document.getElementById('loginForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('jwtToken', data.token);
            window.location.href = '/dashboard';
        } else {
            alert('Invalid credentials');
        }
    } catch (error) {
        console.error('Login failed:', error);
        alert('An error occurred during login. Please try again later.');
    }
});
```