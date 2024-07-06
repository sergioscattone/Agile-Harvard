document.addEventListener('DOMContentLoaded', function () {
    const style = document.createElement('style');
    style.textContent = `
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        body {
            font-family: 'Roboto', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 600px;
            width: 100%;
            animation: fadeIn 1s ease-in-out;
        }

        h1 {
            margin-bottom: 30px;
            color: #333;
            font-weight: 700;
            font-size: 24px;
        }

        .exercise-list {
            text-align: left;
        }

        .exercise-list ul {
            list-style: none;
            padding: 0;
        }

        .exercise-list li {
            margin-bottom: 15px;
        }

        .exercise-list a {
            display: inline-block;
            background-color: #04AA6D; /* Default Green */
            border: none;
            color: white;
            padding: 15px;
            text-align: center;
            text-decoration: none;
            font-size: 18px;
            border-radius: 10px;
            transition: background-color 0.3s ease, transform 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%; /* Ensure all buttons are the same length */
            box-sizing: border-box;
        }

        .exercise-list a:nth-child(odd) {
            background-color: #1E90FF; /* Blue */
        }

        .exercise-list a:nth-child(even) {
            background-color: #FF6347; /* Red */
        }

        .exercise-list a:hover {
            transform: translateY(-2px);
            opacity: 0.9;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    `;
    document.head.appendChild(style);
});