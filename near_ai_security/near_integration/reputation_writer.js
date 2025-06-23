const nearAPI = require("near-api-js");
const fs = require("fs");
require("dotenv").config();

(async () => {
  const { connect, KeyPair, keyStores } = nearAPI;

  const keyStore = new keyStores.InMemoryKeyStore();
  const keyPair = KeyPair.fromString(process.env.NEAR_PRIVATE_KEY);
  await keyStore.setKey("testnet", process.env.NEAR_ACCOUNT_ID, keyPair);

  const near = await connect({
    networkId: "testnet",
    keyStore,
    nodeUrl: "https://rpc.testnet.near.org",
    walletUrl: "https://wallet.testnet.near.org",
  });

  const account = await near.account(process.env.NEAR_ACCOUNT_ID);
  const audit = JSON.parse(fs.readFileSync("latest_audit.json", "utf-8"));

  await account.functionCall({
    contractId: process.env.REPUTATION_CONTRACT_ID,
    methodName: "set_score",
    args: { contract_id: audit.contract_id, score: audit.score },
    gas: "30000000000000",
    attachedDeposit: "0",
  });

  console.log(`✅ Score ${audit.score} for ${audit.contract_id} pushed to NEAR.`);
})();
