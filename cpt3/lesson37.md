
#### 1. `list`基本操作

|操作说明|示例|结果|
|:--|:--|:--|
|`[:]` 提取整个列表 | `[1,2,3][:]` | `[1,2,3]`|
|`[start:]` 从`start`索引开始到最后 | `[1,2,3][1:]` | `[2,3]`|
|`[:end]` 从0索引开始到`end-1`索引 | `[1,2,3][:2]` | `[1,2]`|
|`[start:end]` 从`start`到`end-1` | `[1,2,3,4,5][1:4]` | `[2,3,4]`|
|`[start:end:step]` 从`start`到`end-1`,步长为`step` | `[1,2,3,4,5,6,7,8,9,10][1:7:2]` | `[2,4,6]`|


|操作说明|示例|结果|
|:--|:--|:--|
| `[1,2,3][-2:]` | 倒数3个 | `[2,3]`|
