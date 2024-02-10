[@julep/sdk](../README.md) / [Modules](../modules.md) / [index](../modules/index.md) / [JulepApi](../modules/index.JulepApi.md) / Tool

# Interface: Tool

[index](../modules/index.md).[JulepApi](../modules/index.JulepApi.md).Tool

## Table of contents

### Properties

- [definition](index.JulepApi.Tool.md#definition)
- [id](index.JulepApi.Tool.md#id)
- [type](index.JulepApi.Tool.md#type)

## Properties

### definition

• **definition**: [`FunctionDef`](index.JulepApi.FunctionDef.md)

Function definition and parameters

#### Defined in

[src/api/api/types/Tool.d.ts:9](https://github.com/julep-ai/samantha-dev/blob/1a65618/sdks/js/src/api/api/types/Tool.d.ts#L9)

___

### id

• **id**: `string`

Tool ID

#### Defined in

[src/api/api/types/Tool.d.ts:11](https://github.com/julep-ai/samantha-dev/blob/1a65618/sdks/js/src/api/api/types/Tool.d.ts#L11)

___

### type

• **type**: [`ToolType`](../modules/index.JulepApi.md#tooltype)

Whether this tool is a `function` or a `webhook` (Only `function` tool supported right now)

#### Defined in

[src/api/api/types/Tool.d.ts:7](https://github.com/julep-ai/samantha-dev/blob/1a65618/sdks/js/src/api/api/types/Tool.d.ts#L7)