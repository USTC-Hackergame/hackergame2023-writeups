(function () {
    if (IntersectionObserver === undefined || fetch === undefined) {
        alert('Your browser does not support this challenge!');
        window.location.reload();
        return;
    }

    function errorHandle(err) {
        localStorage.setItem('token', "");
        alert(err);
        console.error(err);
        window.location.reload();
        throw err;
    }
    let params = new URLSearchParams(location.search);
    let token = params.get('token') || localStorage.getItem('token');
    if (!token) {
        token = prompt('Please give me your token:');
        if (!token) {
            errorHandle("No token provided!")
        }
    } else {
        history.replaceState(null, '', location.pathname); // Hide the token from the URL
    }

    async function validateToken(token) {
        // Validate the token
        let res = await fetch(`/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ token }),
        });
        if (res.status !== 200) {
            errorHandle("Invalid token!")
        }
        localStorage.setItem('token', token);
    }

    validateToken(token);

    async function getFlag(token) {
        // Generate the flag based on user's token
        let hash = CryptoJS.SHA256(`dEEper_@nd_d@rKer_${token}`).toString();
        return `flag{T1t@n_${hash.slice(0, 32)}}`;
    }
    let flag_el = document.getElementById('titan');
    let goTop = document.getElementById('go-top');
    let mid = document.querySelector('.mid');
    let cnt = 0;
    let n = 0;
    function randomBubble() {
        let i = Math.random();
        if (i > 0.1) {
            return ' ';
        } else {
            i = Math.random() * 60 - 30;
            let isBig = Boolean(i % 2);
            let bubble = isBig ? 'O' : 'o';
            if (i < 0) {
                return bubble + ' '.repeat(-i);
            } else {
                return ' '.repeat(i) + bubble;
            }
        }
    }
    function insert() {
        cnt = (cnt + 1) % 100;
        n += !cnt;
        let add = mid.cloneNode(false);
        add.textContent = cnt ? randomBubble() : `${n}00 m`;
        flag_el.before(add);
        return add;
    }
    const io = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                observer.unobserve(entry.target);
                observer.observe(insert());
            }
        });
    });
    io.observe(mid);
    for (let i = 0; i < 20; i++) {
        io.observe(insert());
    }
    io.observe(flag_el);
    getFlag(token).then(flag => {
        window.setTimeout(() => {
            let s = `
                               /
                               \\
                               |
                             __|__
                            |     \\
                                    /
     ____  _________________|___ ___\\__________/ ____
    <   /                                            \\____________  |
     /         ${flag}       \\ (_)
~~~~~~     O       O       O                                       >=)~~~~~~~
       \\_______/ ____________\\  /_________________________________/ (_)`;
            goTop.click();
            flag_el.textContent = s;
        }, 500);
    });
    let vh = window.visualViewport.height;
    function calc() {
        // Non-linear percent calculation
        let percent = Math.atan(window.scrollY / vh / 10) * 2 / Math.PI;
        document.body.style.setProperty('--percent', 1 - percent);
    }
    document.addEventListener("scroll", calc);
    window.addEventListener("resize", e => {
        vh = window.visualViewport.height;
        calc();
    });
    calc();
})();
