.. _CRSC:

Configuring Remote Systems for Collection
=========================================

This section outlines some techniques that may need to be done on a remote system to get the full functionality of |cyTriage|. 

|cyTriage| will work without any of these being performed, but you will have better results if you follow them.

Allow Remote Connections with Local Accounts
--------------------------------------------

If you are using a local administrator account on the remote system (instead of a domain account) 
and you want |cyTriage| to push the collection tool using the **Live Collection - Automatic** mode, 
then you will need to enable remote administration for local accounts on that system. 

1. Run the ``regedit.exe`` Windows program on the target computer. 
2. Navigate to the ``HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System`` node. 
3. Right click on the System node to add a **REG_DWORD** value with a name of ``LocalAccountTokenFilterPolicy`` (no quotes) and a value of ``1``.
4. Reboot the system so new policy is applied
