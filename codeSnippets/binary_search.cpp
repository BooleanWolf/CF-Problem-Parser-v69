ll binary_search(vector<ll> arr, ll k)
{
    ll l = 0;
    ll s = arr.size();
    cout << s << endl;
    ll r = s - 1;

    while (l <= r)
    {
        ll m = l + (r - 1) / 2;

        if (arr[m] == k)
        {
            return m;
        }

        if (arr[m] < k)
            l = m + 1;

        else
            r = m - 1;
    }
    return -1;
}

// ll ind = binary_search(arr, data);