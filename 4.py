from collections import defaultdict,deque
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # 构建图，使用字典存储每个节点的邻接列表和权重
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        # 初始化距离列表，设置为无穷大
        distance=[float('inf')]*(n+1)
        # 节点k的距离初始化为0
        distance[k]=0
        # 使用队列进行广度优先搜索
        queue=deque([k])
        while queue:
            current_node=queue.popleft()
            for neighbor,weight in graph[current_node]:
                # 计算通过当前节点到达邻居节点的距离
                new_distance=distance[current_node]+weight
                # 如果新距离更短，则更新距离并加入队列
                if new_distance<distance[neighbor]:
                    distance[neighbor]=new_distance
                    queue.append(neighbor)
         # 检查是否有节点未被访问，即无法到达
        if any(dist == float('inf') for dist in distance[1:]):return -1
         # 返回最后一个节点到达的时间
        return max(distance[1:])
sol=Solution()
print(sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))    