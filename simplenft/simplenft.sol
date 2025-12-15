// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "node_modules/@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "node_modules/@openzeppelin/contracts/access/Ownable.sol";

contract SimpleNFT is ERC721URIStorage, Ownable
{
    uint public tokencounter;
    constructor () public ERC721 ("Badge1","NFTBadges")
    {
        tokencounter=0;         //count of total tokens minted
    }

    function CreateCollectible(string memory tokenuri) public returns (uint)
    {
        
        uint newtokenid=tokencounter;
        string memory tokenuri="ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json";
        _safeMint(msg.sender, newtokenid);
        _setTokenURI(newtokenid, tokenuri);
        tokencounter=tokencounter+1; 
        return newtokenid;
    }
}