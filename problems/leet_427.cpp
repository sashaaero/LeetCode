class Solution {
	public:
			Node* construct(vector<vector<int>>& grid) {
					return quadTree(grid, 0, grid.size()-1, 0, grid.size()-1);
			}

			Node* quadTree(vector<vector<int>>& grid, int is, int ie, int js, int je){
					bool same = true;
					for(int i = is; i <= ie && same; ++i){
							for(int j = js; j <= je && same; ++j){
									if(grid[i][j] ^ grid[is][js]) same = false;
							}
					}
					if(same){
							return new Node(grid[is][js], true, nullptr, nullptr, nullptr, nullptr);
					}
					return new Node(0, false, quadTree(grid, is, (is + ie)/2, js, (js + je)/2), quadTree(grid, is, (is + ie)/2, (js + je)/2 + 1, je), quadTree(grid, (is + ie)/2 + 1, ie, js, (js + je)/2), quadTree(grid, (is + ie)/2 + 1, ie, (js + je)/2 + 1, je));
			}
	};
