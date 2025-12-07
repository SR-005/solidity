// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleNFT is ERC721
{
    uint public tokencounter;
    constructor () public ERC721 ("Badge1","NFTBadges")
    {
        tokencounter=0;
    }

    function CreateCollectible() public returns (uint)
    {
        uint newtokenid=tokencounter;
        _safeMint(msg.sender, newtokenid);
        tokencounter=tokencounter+1;
        return newtokenid;
    }
}