### Problem 2
<ol type="a">
  <li>Design Tests
    <ol type="i">
    <li>It is not possible to have path coverage at all since there are impossible paths, however if we omit those, we can use these inputs to get to all reachable paths without condition coverage
      1. (x = -1, y = 0, z = 0)
      2. (x = -1, y = 2, z = 0)
      3. (x = 1, y = 2, z = 0)
      </li>
      <li>Again coverage is incomplete since one of them is impossible to satisfy based on previous conditions, and since z is unchanged condition coverage is not met.
      1. (x = -1, y = 0, z = 0)
      2. (x = -1, y = 2, z = 0)
      3. (x = 1, y = 2, z = 0)
      </li>
      <li>Covering the conditions carefully we can avoid all the paths
      1. (x = 1, y = 0, z = 0)
      2. (x = 1, y = 2, z = -1)
      3. (x = -1, y = 2, z = 0)
      </li>
    </ol>
  </li>
  <li>Running Tests
    <ol type="i">
    <li>No statement coverage is not possible, lines 12,13,14 can not be reached, since it follows an impossible condition</li>
    <li>yes using the input from a.iii above</li>
    <li>No, since the condition on line 11 contradicts line 3</li>
  </li>
</ol>