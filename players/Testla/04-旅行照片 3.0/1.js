const dates = [
    '2023-06-02',
    // '2023-06-03',
    // '2023-06-04',
    // '2023-06-09',
    // '2023-06-10',
    // '2023-06-11',
    // '2023-06-15',
    // '2023-06-16',
    // '2023-06-17',
    // '2023-06-18',
    // '2023-06-23',
    // '2023-06-24',
    // '2023-06-25',
];
const acronyms = [
    // 'NBI',
    // 'NBIOC',
    // 'BLC',
    // 'OC',
    // 'ICEP',
    'ICRR',
];

function dateToString(date) {
    return [
        (date.getFullYear() + '').padStart(4, '0'),
        (date.getMonth() + '').padStart(2, '0'),
        (date.getDate() + '').padStart(2, '0'),
    ].join('-');
}

// for (const date of dates) {
let date = new Date(2023, 6, 1);
while (date.getMonth() < 11) {
    for (const acronym of acronyms) {
        fetch(
            'http://202.38.93.111:12345/',
            {
                "method": "POST",
                "headers": {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                },
                "body": btoa(`Answer1=${dateToString(date)}&Answer2=${acronym}`) + '.txt',
            }
        );
    }
    date.setDate(date.getDate() + 1);
}
