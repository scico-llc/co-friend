const {default: Web3} = require("web3");

const NFT_CONTRACT = "0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9"
const REGISTRY_CONTRACT_ADDRESS = "0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0";
const PUBLIC_KEY = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266";
const PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80";
const PROVIDER_URL = "http://localhost:8545";


async function linkAccount() {
    const web3 = new Web3(PROVIDER_URL);
    const contract = require("../../artifacts/contracts/AccountRegistry.sol/AccountRegistry.json");
    const accountRegistry = new web3.eth.Contract(contract.abi, REGISTRY_CONTRACT_ADDRESS);

    const nonce = await web3.eth.getTransactionCount(PUBLIC_KEY, "latest");
    const tx = {
        from: PUBLIC_KEY,
        to: REGISTRY_CONTRACT_ADDRESS,
        nonce: nonce,
        gas: 500000,
        gasPrice: 540505584,
        data: accountRegistry.methods.createAccount(NFT_CONTRACT, 1).encodeABI(),
    };

    const signPromise = web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);

    signPromise
        .then((signedTx) => {
            const tx = signedTx.rawTransaction;
            if( tx !== undefined ){
                web3.eth.sendSignedTransaction(tx, function(err, hash) {
                    if( !err ) {
                        console.log("The hash of your transaction is:", hash);
                    } else {
                        console.log("Something went wrong when submittion your transaction:", err);
                    }
                });
            }
            console.log("row36");
        })
        .catch( (err) => {
            console.log("Promise failed:", err);
        });
}

linkAccount();