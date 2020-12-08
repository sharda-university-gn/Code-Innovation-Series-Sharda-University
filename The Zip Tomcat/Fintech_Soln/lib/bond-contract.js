/*
 * SPDX-License-Identifier: Apache-2.0
 */

'use strict';

const { Contract } = require('fabric-contract-api');

class BondContract extends Contract {

    async bondExists(ctx, bondId) {
        const buffer = await ctx.stub.getState(bondId);
        return (!!buffer && buffer.length > 0);
    }

    async createBond(ctx, bondId, value) {
        const exists = await this.bondExists(ctx, bondId);
        if (exists) {
            throw new Error(`The bond ${bondId} already exists`);
        }
        const asset = { value };
        const buffer = Buffer.from(JSON.stringify(asset));
        await ctx.stub.putState(bondId, buffer);
    }

    async readBond(ctx, bondId) {
        const exists = await this.bondExists(ctx, bondId);
        if (!exists) {
            throw new Error(`The bond ${bondId} does not exist`);
        }
        const buffer = await ctx.stub.getState(bondId);
        const asset = JSON.parse(buffer.toString());
        return asset;
    }

    async updateBond(ctx, bondId, newValue) {
        const exists = await this.bondExists(ctx, bondId);
        if (!exists) {
            throw new Error(`The bond ${bondId} does not exist`);
        }
        const asset = { value: newValue };
        const buffer = Buffer.from(JSON.stringify(asset));
        await ctx.stub.putState(bondId, buffer);
    }

    async deleteBond(ctx, bondId) {
        const exists = await this.bondExists(ctx, bondId);
        if (!exists) {
            throw new Error(`The bond ${bondId} does not exist`);
        }
        await ctx.stub.deleteState(bondId);
    }

}

module.exports = BondContract;
