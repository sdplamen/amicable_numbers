function sumProperDivisors(n) {
    let divisionSum = 1;
    const limit = Math.floor(Math.sqrt(n)) + 1;
    for (let i = 2; i < limit; i++) {
        if (n % i === 0) {
            divisionSum += i;
            if (i !== n / i) {
                divisionSum += n / i;
            }
        }
    }
    return divisionSum;
}

function findAmicablePairs(limit) {
    const amicablePairs = [];
    for (let a = 2; a <= limit; a++) {
        const b = sumProperDivisors(a);
        if (a < b && b <= limit && sumProperDivisors(b) === a) {
            amicablePairs.push([a, b]);
        }
    }
    return amicablePairs;
}

function calculateAmicable() {
    const limitInput = document.getElementById('limit').value;
    const errorElement = document.getElementById('error');
    const resultElement = document.getElementById('result');
    errorElement.textContent = '';
    resultElement.innerHTML = '';

    const limit = parseInt(limitInput);
    if (isNaN(limit) || limit < 2) {
        errorElement.textContent = 'Please enter a valid integer greater than or equal to 2.';
        return;
    }

    const amicablePairs = findAmicablePairs(limit);
    if (amicablePairs.length === 0) {
        resultElement.innerHTML = `<p>No amicable numbers found up to ${limit}.</p>`;
    } else {
        let resultHTML = `<p>Amicable numbers up to ${limit}:</p><ul>`;
        amicablePairs.forEach(pair => {
            resultHTML += `<li>${pair[0]} and ${pair[1]}</li>`;
        });
        resultHTML += '</ul>';
        resultElement.innerHTML = resultHTML;
    }
}