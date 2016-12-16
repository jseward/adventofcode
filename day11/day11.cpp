#include <bitset>
#include <unordered_set>
#include <array>
#include <iostream>

using namespace std;

static const int ELEMENT_COUNT = 7;
static const int FLOOR_COUNT = 4;

class collection {
public:
	bitset<ELEMENT_COUNT * 2> items;

	bool has_generator(int i) const {
		return items[i * 2];
	}

	bool has_microchip(int i) const {
		return items[(i * 2) + 1];
	}

	bool has_any_generator() const {
		for (int i = 0; i < ELEMENT_COUNT; ++i) {
			if (has_generator(i)) {
				return true;
			}
		}
		return false;
	}

	bool is_valid() const {
		for (int i = 0; i < ELEMENT_COUNT; ++i) {
			if (has_microchip(i) && !has_generator(i)) {
				if (has_any_generator()) {
					return false;
				}
			}
		}
		return true;
	}

	bool operator==(const collection& rhs) const {
		return items == rhs.items;
	}
};

template <>
struct hash<collection> {
	size_t operator()(const collection& k) const {
		return k.items.hash();
	}
};

class state {
public:
	typedef array<collection, FLOOR_COUNT> floor_array;

	int elevator;
	floor_array floors;

	bool operator==(const state& rhs) const {
		return
			elevator == rhs.elevator &&
			floors == rhs.floors;
	}
};

//http://stackoverflow.com/questions/2590677/how-do-i-combine-hash-values-in-c0x
template <class T>
inline void hash_combine(size_t& seed, const T& v) {
	hash<T> hasher;
	seed ^= hasher(v) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
}

template <>
struct hash<state> {
	size_t operator()(const state& k) const {
		size_t seed = 0;
		hash_combine(seed, k.elevator);
		for (const auto& floor : k.floors) {
			hash_combine(seed, floor);
		}
		return seed;
	}
};

typedef unordered_set<state> state_set;

vector<pair<int, int>> make_item_pairs(const collection& c) {
	vector<pair<int, int>> pairs;
	for (size_t i = 0; i < c.items.size(); ++i) {
		if (c.items[i]) {
			pairs.push_back(pair<int, int>(i, -1));
			for (size_t j = i + 1; j < c.items.size(); ++j) {
				if (c.items[j]) {
					pairs.push_back(pair<int, int>(i, j));
				}
			}
		}
	}
	return pairs;
}

state make_new_state(const state& s, int new_elevator, int item_0, int item_1) {
	state new_state = s;
	new_state.elevator = new_elevator;
	new_state.floors[s.elevator].items.set(item_0, false);
	new_state.floors[new_elevator].items.set(item_0, true);
	if (item_1 != -1) {
		new_state.floors[s.elevator].items.set(item_1, false);
		new_state.floors[new_elevator].items.set(item_1, true);
	}
	return new_state;
}

void make_next_states_in_direction(state_set& next_states, const state_set& visited_states, const state& s, int direction) {
	int new_elevator = s.elevator + direction;
	if (new_elevator >= 0 && new_elevator < FLOOR_COUNT) {
		for (auto item_pair : make_item_pairs(s.floors[s.elevator])) {
			auto new_state = make_new_state(s, new_elevator, item_pair.first, item_pair.second);
			if (
				new_state.floors[s.elevator].is_valid() && 
				new_state.floors[new_elevator].is_valid() &&
				visited_states.find(new_state) == visited_states.end()) {
				next_states.insert(new_state);
			}
		}
	}
}

void make_next_states(state_set& next_states, const state_set& visited_states, const state& s) {
	make_next_states_in_direction(next_states, visited_states, s, -1);
	make_next_states_in_direction(next_states, visited_states, s, +1);
}

void print_state(const state& s) {
	cout << "elevator = " << s.elevator << endl;
	for (auto f : s.floors) {
		for (size_t i = 0; i < f.items.size(); ++i) {
			cout << f.items[i] ? "x" : ".";
		}
		cout << endl;
	}
}

int main() {
	state initial_state;
	initial_state.elevator = 0;
	initial_state.floors.at(0).items.set(0, true); //TH = 0
	initial_state.floors.at(0).items.set(1, true);
	initial_state.floors.at(0).items.set(2, true); //PL = 2
	initial_state.floors.at(0).items.set(4, true); //ST = 4
	initial_state.floors.at(1).items.set(3, true);
	initial_state.floors.at(1).items.set(5, true);
	initial_state.floors.at(2).items.set(6, true); //PR = 6
	initial_state.floors.at(2).items.set(7, true);
	initial_state.floors.at(2).items.set(8, true); //RU = 8
	initial_state.floors.at(2).items.set(9, true);
	initial_state.floors.at(0).items.set(10, true); //EL = 10
	initial_state.floors.at(0).items.set(11, true);
	initial_state.floors.at(0).items.set(12, true); //DI = 12
	initial_state.floors.at(0).items.set(13, true);

	state final_state;
	final_state.elevator = 3;
	for (int i = 0; i < ELEMENT_COUNT * 2; ++i) {
		final_state.floors.at(3).items.set(i, true);
	}

	state_set current_states;
	state_set next_states;
	state_set visited_states;

	int step = 0;
	current_states.insert(initial_state);
	while (current_states.find(final_state) == current_states.end()) {
		cout << "STEP = " << step << " (" << current_states.size() << ")" << endl;
		for (const auto& s : current_states) {
			make_next_states(next_states, visited_states, s);
		}
		visited_states.insert(next_states.begin(), next_states.end());
		current_states = next_states;
		next_states.clear();
		step++;
	}

	cout << "FINAL STEP = " << step << endl;

	return 0;
}
